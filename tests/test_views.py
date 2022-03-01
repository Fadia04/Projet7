from tests.conftest import client


def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200
def test_should_status_code_nok(client):
	response = client.get('/')
	assert response.status_code == 404

def mock_get_response(*args, **kwargs):
	result = {
                "status": "ok",
                "latitude": 48.8421379, 
                "longitude": 2.3219514,
                "summary": "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.",
            
                "url": "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche",
        
            }
	return result

def test_should_status1_code_ok(client):
	response = client.post('/question', data={'user_question': 'Où se trouve le Panthéon Paris?'})
	assert response.status_code == 200
def test_should_status1_code_nok(client):
	response = client.post('/question')
	assert response.status_code == 404

def test_should_return_user_question():
	user_question = 'où se trouve le panthéon paris?'
	response = client.post('/question', data={'user_question': user_question})
	data = response.data.decode()
	assert data == 'Où se trouve le Panthéon Paris?'

def test_should_return_response(monkeypatch):
	response = client.post('/question', data={'response': ' '})
	data = response.data.decode()
	monkeypatch.setattr("classes.manager.Manager.get_response", mock_get_response)
	
	assert data.status_code== "OK"