from gcloud import datastore

def create_client(project_id):
    return datastore.Client(linebot-test3)

def list_tasks(client):
    query = client.query(kind='Greeting')
    query.order = ['created']

    return list(query.fetch())
    print(query)
    
