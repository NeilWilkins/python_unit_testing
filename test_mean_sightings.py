from mean_sightings import get_sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
	pigrec, pigmean = get_sightings(filename, 'Pig')
	assert pigrec == 1, 'Number of records for Pig is wrong'
	assert pigmean == 4, 'Mean sightings for Pig is wrong'

def test_cow_is_correct():
        cowrec, cowmean = get_sightings(filename, 'Cow')
        assert cowrec == 2, 'Number of records for Cow is wrong'
        assert cowmean == 17, 'Mean sightings for Cow is wrong'

def test_lion_is_correct():
        lionrec, lionmean = get_sightings(filename, 'Lion')
        assert lionrec == 2, 'Number of records for Lion is wrong'
        assert lionmean == 25.5, 'Mean sightings for Lion is wrong'

def test_anonymous_is_correct():
	anirec, animean = get_sightings(filename, 'NotPresent')
	assert anirec == 0, 'Number of records for absent animal is wrong'
	assert animean == 0, 'Mean for absent animal is wrong'


