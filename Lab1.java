//Lab 1 ICS 45J 
//Submitted by Roshan Suasin rsuasin 41262572 and
//			   Shah Masood ssmasood 16608754

public class Lab1{
	public static void main(String[] args){
		
		Movie example = new Movie();
		example.setDuration(330);
		example.setPrice(19.99);
		example.setTitle("Harry Potter and the Goblet of Fire");
		example.setYear(2000);
		example.setDirector("J.K.", "Rowling", 1965, 7);
		System.out.println(example.toString());
		Movie copy = new Movie(example);
		System.out.println("\nCOPY\n" + copy.toString());
		
		Director copyDir = copy.getDirector();
		for(int i = 0; i < 5; i++){
			copyDir.increaseFilms();
		}
	
		System.out.println("\nUPDATED RELEASES BY 5 COPY\n" + copy.toString());
		System.out.println("\nORIGINAL MOVIE\n" + example.toString());
	}
}