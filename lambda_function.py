from src.pipeline import run_pipeline

def lambda_handler(event, context):
    try:
        print("Lambda triggered")

        run_pipeline()

        return {
            "statusCode": 200,
            "body": "Pipeline executed successfully"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }