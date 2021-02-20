import java.io.*;

public class StringCal{
	public static void main(String args[]){
		ReturnZeroIfNull();
		ReturnNumbersIfNotNull();
	}
	
	public static int add(String str){
		
		return 0;
	}
	
	public static void ReturnZeroIfNull(){
		int sum = 0;
		int val;
		val = StringCal.add("");
		compare(sum,val);
		
	}
	
	public static void ReturnNumbersIfNotNull(){
		int sum = 12;
		int val = StringCal.add("12");
		compare(sum,val);
	}
	
	public static void compare(int sum, int val){
		if(sum == val){
			System.out.println("OK");
		}
		else{
			System.out.println("NOT OK");
		}
	}
		
}
