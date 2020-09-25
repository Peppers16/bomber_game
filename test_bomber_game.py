import pytest
import bomber_game as bg


@pytest.fixture()
def height_vector():
    return [10,8,5,3,1,0,11,15,2,0,5]


class TestSkyline:
    def test_basic_skyline(self, height_vector):
        basic_skyline = bg.Skyline(height_list=height_vector)
        assert basic_skyline.buildings[0].height == 10
        assert basic_skyline.buildings[0].index == 0
        assert basic_skyline.buildings[-1].height == 5


class TestMain:
    def test_main_loop(self, height_vector):
        bg.main(height_vector)
