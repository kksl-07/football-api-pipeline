from pydantic import ValidationError

from football_api_pipeline.models.football.transfers import Transfer
from football_api_pipeline.services.api import API

API_KEY = ""


def test_run_api_query():
    try:
        t_obj = Transfer(transfer_obj={"team": "463"})

        # query_params = p_obj.top_scores_obj.__dict__
        query_params = t_obj.transfer_obj.__dict__
        api = API()
        df = api.run_api_pipeline(
            url="https://v3.football.api-sports.io",
            endpoint_name=t_obj.endpoint_name,
            api_key=API_KEY,
            api_query_params=query_params,
        )
        print(df)
    except ValidationError as e:
        print(repr(e.errors()))
