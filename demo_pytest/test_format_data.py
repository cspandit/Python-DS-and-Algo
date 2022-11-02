import pytest
import format_data

@pytest.fixture
def example_people_data():
	people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

	return people

def test_format_data_for_display(example_people_data):
	assert format_data.format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
	assert format_data.format_data_for_excel(example_people_data) == """given,family,title
	Alfonsa,Ruiz,Senior Software Engineer
	Sayid,Khan,Project Manager"""