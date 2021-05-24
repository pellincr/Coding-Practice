package uniqueArrayProducts;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class uniqueArrayProductsTest {

	@Test
	void test() {
		int[] lon1 = {1,2,3,4,5};
		int[] alon1 = {120,60,40,30,24};
		int[] lon2 = {1,5,7,3};
		int[] alon2 = {105,21,15,35};
		//arrayProduct Tests
		assertEquals(uniqueArrayProducts.arrayProduct(lon1), 120);
		assertEquals(uniqueArrayProducts.arrayProduct(lon2), 105);
		//uniqueArrayProduct Tests
		assertArrayEquals(uniqueArrayProducts.uniqueArrayProduct(lon1), alon1);
		assertArrayEquals(uniqueArrayProducts.uniqueArrayProduct(lon2), alon2);
	}

}
