package Question_2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SolutionTest {

	@Test
	void test() {
		String[] a = {"aa"};
		assertEquals(Solution.isPalindrome("aba"), true);
		assertEquals(Solution.isPalindrome("abb"), false);
		assertEquals(Solution.isPalindrome("aa"), true);
		
		assertEquals(Solution.Palindromes("aa"), a);
	}

}
