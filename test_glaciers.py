import pytest
from utils import check_id, check_lat_value, check_lon_value, check_year, check_annual_value
from glaciers import Glacier, GlacierCollection

def test_id():
    assert check_id('123')== False
    assert check_id('8t123')== False
    assert check_id('123--')== False
    assert check_id('12345')== True
def test_lat_value():
    assert check_lat_value(-91)== False
    assert check_lat_value('-91')== False
    assert check_lat_value(90)== True
    assert check_lat_value('0')== True
def test_lon_value():
    assert check_lon_value(-181)== False
    assert check_lon_value('-181')== False
    assert check_lon_value(180)== True
    assert check_lon_value('0')== True
def test_year():
    assert check_year(1998) == True
    assert check_year('1998') == True
    assert check_year('0') == False
    assert check_year('-1900') == False
    assert check_year('19000') == False
def test_annual_value():
    assert check_annual_value(1900) == True
    assert check_annual_value(19.00) == True
    assert check_annual_value(-1900) == True
    assert check_annual_value('-19.00') == True
    assert check_annual_value('') == False
    assert check_annual_value('---') == False

def test_add_mess_data():
    my_glacier = Glacier('01657', 'DE LOS TRES', 'AR', -49.33, -73.0, 544)
    my_glacier.add_mass_balance_measurement('1991','190',False)
    my_glacier.add_mass_balance_measurement('1991', '190', False)
    my_glacier.add_mass_balance_measurement('1992', '-190', True)
    my_glacier.add_mass_balance_measurement('1992', '190', True)
    assert my_glacier.years == ['1991','1992']
    assert my_glacier.mass_balances == ['190','0']

test_id()
test_lat_value()
test_lon_value()
test_year()
test_annual_value()
test_add_mess_data()