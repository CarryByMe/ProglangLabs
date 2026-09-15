import java.util.Scanner;	

public class Main{
	public static void main(String args){
		int x, s = 0;
		Scanner in = new Scanner(System.in);
		x = in.nextInt();
		for(int i = 0; i < 123; i++){
			s+=x;
		}
		System.out.println(s);
	}
}
		