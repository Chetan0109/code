import java.io.*;
import java.lang.*;

public class StringCal{
	public static void main(String args[]){
		
		ReturnZeroIfNull();
		ReturnNumbersIfNotNull();
		ReturnSumIfDelimByComma();
		
	}
	
	public static int add(String str){
		if(str == ""){
			return 0;
		}
		else if(str.contains(",")){
			String[] numbers = str.split(",");
			int j = 0;
			for(int i = 0;i<numbers.length;i++){
				j = j + Integer.parseInt(numbers[i]);
			}
			return j;
		}
		else{
			return Integer.parseInt(str);
		}
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
	
	public static void ReturnSumIfDelimByComma(){
		int sum = 6;
		int val;
		String s = "1,2,3";
		val = add(s);
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
