import json

import pandas as pd
import requests
from requests.models import Response

from football_api_pipeline.utils.flatten import flatten_json
from football_api_pipeline.utils.logger import get_logger

logger = get_logger("info")


class API:
    @staticmethod
    def _build_api_url(url: str, endpoint_name: str) -> str:
        api_query = f"{url}/{endpoint_name}/"
        logger.info(f"Query to run on Football API: {api_query}")
        return api_query

    @staticmethod
    def _get_api_response(url: str, api_key: str, params: dict) -> requests.Response:
        headers = {"X-RapidAPI-Key": api_key, "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
        response = Response()

        try:
            response = requests.get(url=url, headers=headers, params=params, timeout=10)
        except requests.exceptions.HTTPError as http_err:
            logger.info(f"HTTP error occurred: {http_err} in {__name__}")
        except requests.exceptions.Timeout:
            logger.info("Request timed out.")
        except requests.exceptions.RequestException as err:
            logger.info(f"An error occurred: {err}")
        except ValueError as e:
            logger.info(e)

        return response

    @staticmethod
    def _process_api_response(resp) -> pd.DataFrame:
        final_df = pd.DataFrame()
        try:
            res = json.loads(resp.text)
            final_df = pd.DataFrame()
            for act in res["response"]:
                flatten_resp = flatten_json(act)
                df = pd.DataFrame([flatten_resp])
                final_df = pd.concat([final_df, df], ignore_index=True)
        except json.JSONDecodeError as e:
            logger.info(f"Invalid JSON syntax: {e}")

        return final_df

    def run_api_pipeline(self, url: str, endpoint_name: str, api_key: str, api_query_params: dict) -> pd.DataFrame:
        logger.info(f"Start get {endpoint_name} response from API")
        api_url = self._build_api_url(url=url, endpoint_name=endpoint_name)
        resp = self._get_api_response(url=api_url, api_key=api_key, params=api_query_params)
        logger.info(f"End get {endpoint_name} response from API")

        logger.info("Start processing api response")

        df = self._process_api_response(resp)

        logger.info("End processing api response")

        return df
