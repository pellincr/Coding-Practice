package upToK;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class upToKTest {

	@Test
	void test() {
		int[] lon1 = {10,15,3,7};
		int[] lon2 = {10,5,4,3};
		int[] lon3 = {10,5,4,3,10};
		assertEquals(upToK.addUpToK(17,lon1),true);
		assertEquals(upToK.addUpToK(20, lon2),false);
		assertEquals(upToK.addUpToK(20, lon3),true);
	}

}
