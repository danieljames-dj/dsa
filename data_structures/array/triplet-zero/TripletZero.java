import java.util.HashMap;
import java.util.Scanner;

public class TripletZero {
	
	private int[] getInput() {
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("Enter the length of the array : ");
//		int length = scanner.nextInt();
//		int[] input = new int[length];
//		for (int i = 0; i < length; i++) {
//			input[i] = scanner.nextInt();
//		}
//		scanner.close();
		int[] input = {0, -1, 2, -3, 1};
		return input;
	}
	
	//brute force
	private void getTripletZeroCount_BruteForce(int[] input) {
		for (int i = 0; i < input.length; i++) {
			for (int j = i + 1; j < input.length; j++) {
				for (int k =  j + 1; k < input.length; k++) {
					if (input[i] + input[j] + input[k] == 0) {
						System.out.println(input[i] + " " + input[j] + " " + input[k]);
					}
				}
			}
		}
	}
    
    //hashing
	private void getTripletZeroCount(int[] input) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < input.length; i++) {
            Integer currentCount = hashMap.get(input[i]);
            if (currentCount == null) {
                hashMap.put(input[i], 1);
            } else {
                hashMap.put(input[i], currentCount + 1);
            }
        }
		for (int i = 0; i < input.length; i++) {
			for (int j = i + 1; j < input.length; j++) {
                int k = -(input[i] + input[j]);
                if (hashMap.get(k) != null) {
                    System.out.println(input[i] + " " + input[j] + " " + k);
                }
			}
		}
	}

	public static void main(String args[]) {
		TripletZero tripletZero = new TripletZero();
		int input[] = tripletZero.getInput();
		tripletZero.getTripletZeroCount(input);
	}
}
