package smallestNonexistingPositive;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class smallestNonexistingPositiveTest {

	@Test
	void test() {
		int[] l1 = {3,4,-1,1};
		int[] l2 = {-3,-2,-1,0};
		int[] l3 = {1,2,3,4,5};
		int[] l4 = {2,3,4,5,6};
		assertEquals(smallestNonexistingPositive.smallestNoneistingPositive(l1), 2);
		assertEquals(smallestNonexistingPositive.smallestNoneistingPositive(l2), 1);
		assertEquals(smallestNonexistingPositive.smallestNoneistingPositive(l3), 6);
		assertEquals(smallestNonexistingPositive.smallestNoneistingPositive(l4), 1);
	}

}
