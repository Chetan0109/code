import java.io.*;

public class StringCal{
	public static void main(String args[]){
		ReturnZeroIfNull();
	}
	
	public static int add(String str){
		return 0;
	}
	
	public static void ReturnZeroIfNull(){
		int sum = 0;
		int val;
		val = StringCal.add("");
		if(sum == val){
			System.out.println("OK");
		}
		else{
			System.out.println("NOT OK");
		}
		
	}
		
}