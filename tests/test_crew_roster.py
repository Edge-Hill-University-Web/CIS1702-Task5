from app.crew_roster import assign_crew

def test_assign_crew_captain():
    assert assign_crew("Kirk", "Captain") == "Crew Member Kirk assigned to Captain."

def test_assign_crew_engineer():
    assert assign_crew("Scott", "Chief Engineer") == "Crew Member Scott assigned to Chief Engineer."
