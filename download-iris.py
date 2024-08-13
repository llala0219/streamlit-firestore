from google.cloud import firestore
db = firestore.Client.from_service_account_json("streamlit-test-7cbfd-firebase-adminsdk-33jrv-dc407a1e39.json")
docs = db.collection("iris").stream()
for d in docs:
    print(d.to_dict())