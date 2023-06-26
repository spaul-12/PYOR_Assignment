from flask import Flask
from flask_restful import Resource, Api
from flipside import Flipside
import os
from dotenv import load_dotenv
import requests

#loading the env variable
load_dotenv()

app = Flask(__name__)
api = Api(app)


class TransactionCount(Resource):
    def get(self):
        api_key = os.getenv('secret_key')
        flipside = Flipside(api_key, "https://api-v2.flipsidecrypto.xyz")

        sql = """
        SELECT 
          date_trunc('day',block_timestamp) AS Day,
          count(DISTINCT tx_hash) AS tx_count
        FROM optimism.core.fact_transactions 
        WHERE '2023-06-26' >= block_timestamp - interval '1 year'
        GROUP BY 1
        ORDER BY 1 DESC;
        """
        try:
            query_result_set = flipside.query(sql)
            #print(query_result_set)
            return {"Columns":query_result_set.columns,
                    "Rows":query_result_set.rows
                    }
        except:
            return {'Error':'query unsuccessful'}


class EthereumData(Resource):
    def get(self):
        url='https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=30'
        response = requests.get(url)
        if response.status_code==200:
            return {"message":"successfully fetched"}
        else:
            return {"message":"error in fetching data"}

            


api.add_resource(TransactionCount,'/count')
api.add_resource(EthereumData,'/data')

if __name__ == '__main__':
    app.run(debug=True)