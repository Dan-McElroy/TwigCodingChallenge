import pytest
from splitter import *

def test_provided_example():
	assert split_array([1,2,3,4,5], 3) == [[1,2], [3,4], [5]]

def test_even_split():
	assert split_array([1,2,3,4,5,6,7,8,9], 3) == [[1,2,3], [4,5,6], [7,8,9]]
	
def test_wrong_list_type_raises():
	with pytest.raises(TypeError):
		split_array('1,2,3', 3)

def test_wrong_number_type_raises():
	with pytest.raises(TypeError):
		split_array([1,2,3], 'a')

def test_edge_case():
	assert split_array([1,2,3,4],3) == [[1,2],[3,4],[]]

def test_empty_array():
	assert split_array([], 5) == [[],[],[],[],[]]
