import unittest
import requests_mock
from bitrix_webhook_handler.update_gender import handle_contact_change
from tests import insert_data, delete_data


class TestHandleContactChange(unittest.TestCase):
    @requests_mock.Mocker()
    def test_handle_contact_change_man(self, m):
        insert_data('names_man', {'name': 'Alex'})

        request_data_man= {
            "data": {
                "FIELDS": {
                    "ID": 1,
                    "NAME": "Alex"
                }
            }
        }
        m.post("https://test123/crm.contact.update", json={"result": True})
        handle_contact_change(request_data_man)
        self.assertEqual(m.last_request.json(), {
            "ID": 1,
            "fields": {
                "UF_CRM_1611234567": "Мужчина"
            }
        })

    @requests_mock.Mocker()
    def test_handle_contact_change_woman(self, m):
        insert_data('names_woman', {'name': 'Marina'})

        request_data_woman= {
            "data": {
                "FIELDS": {
                    "ID": 1,
                    "NAME": "Marina"
                }
            }
        }

        m.post("https://test123/crm.contact.update", json={"result": True})
        handle_contact_change(request_data_woman)
        self.assertEqual(m.last_request.json(), {
            "ID": 1,
            "fields": {
                "UF_CRM_1611234567": "Женщина"
            }
        })

    @requests_mock.Mocker()
    def test_handle_contact_change_negative(self, m):
        
        request_data_negative= {
            "data": {
                "FIELDS": {
                    "ID": 2,
                    "NAME": "Андрей"
                }
            }
        }

        m.post("https://test123/crm.contact.update", json={"result": True})
        handle_contact_change(request_data_negative)

        self.assertEqual(m.last_request.json(), {
            "ID": 2,
            "fields": {
                "UF_CRM_1611234567": "Не удалось определить пол"
            }
        })

    def tearDown(self):
        delete_data('names_woman', {'name': 'Marina'})
        delete_data('names_man', {'name': 'Alex'})
        # delete_seeds()

# def delete_seeds():
#     delete_data('names_woman', {'name': 'Marina'})
#     delete_data('names_man', {'name': 'Alex'})

if __name__ == '__main__':
    unittest.main()
