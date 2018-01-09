//Lab 1 ICS 45J 
//Submitted by Roshan Suasin rsuasin 41262572 and
//			   Shah Masood ssmasood 16608754

public class Director
{
	private String first;
	private String last;
	private int dob;
	private int filmsDir;
	
	public Director(String f, String l, int d, int fD){
		first = f;
		last = l;
		dob = d;
		filmsDir = fD;
	}
	
	public Director(Director d){
		first = d.getFirst();
		last = d.getLast();
		dob = d.getDob();
		filmsDir = d.getfilmsDir();
	}
	
	public String getFirst(){
		return first;
	}
	
	public String getLast(){
		return last;
	}
	
	public int getDob(){
		return dob;
	}
	
	public int getfilmsDir(){
		return filmsDir;
	}
	
	public void setFirst(String f){
		first = f;
	}
	
	public void setLast(String l){
		last = l;
	}
	
	public void setDob(int d){
		dob = d;
	}
	
	public void setfilmsDir(int f){
		filmsDir = f;
	}
	
	public void increaseFilms(){
		filmsDir++;
	}
	
}

