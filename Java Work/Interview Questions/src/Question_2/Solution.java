package Question_2;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class Solution {
	
	public static List<String> Palindromes(String s)
	{
		List<String> res = new LinkedList<String>();
		for(int i = 0; i<s.length();i++)
		{
			for(int j = i+2; j<s.length();j++)
			{
				if(isPalindrome(s.substring(i,j)))
				{
					res.add(s.substring(i,j));
				}
			}
		
		}
		return res;
	}
	
	public static boolean isPalindrome(String s) {
		Stack<String> f = new Stack<String>();
		Queue<String> q = new LinkedList<String>();
		String res1 = "";
		String res2 = "";
		
		for(int i = 0; i<s.length();i++)
		{
			f.push(s.substring(i,i+1));
			q.add(s.substring(i,i+1));
		}
		for(int j = 0; j<s.length();j++)
		{
			res1 += f.pop();
			res2 += q.peek();
			q.remove();
		}
		return res1.equals(res2);
	}
}
