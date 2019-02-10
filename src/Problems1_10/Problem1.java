//Statement 
//If we list all the natural numbers below 10 that are multiples of 3 
//or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
//Find the sum of all the multiples of 3 or 5 below 1000.
//-----------------------------------------------------------------
package Problems1_10;
import java.util.ArrayList;

public class Problem1 {
		
	public static void main(String[] args) {
		// Initialize empty ArrayList
		ArrayList<Integer> multiples = new ArrayList<Integer>();
		
		// Go from 1 to 1000 and see if it is a multiple of 3 or 5
		for (int i = 1; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				multiples.add(i);
			}
		}
		
		// Take the sum
		int sum = 0;
		for (int x: multiples) {
			sum = sum + x;
		}
		// Print the result
		System.out.println("The sum of the natural numbers until 1000 which are divisible by 3 or 5 is " + sum);
	}
}