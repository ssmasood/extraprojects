//Lab 1 ICS 45J 
//Submitted by Roshan Suasin rsuasin 41262572 and
//			   Shah Masood ssmasood 16608754

public class Movie
{
	private int year;
	private int duration;
	private double price;
	private String title;
	private Director dir;

	public Movie(){
		
	}
	
	public Movie(int y, int d, double p, String t)
	{
		year = y;
		duration = d;
		price = p;
		title = t;
	}
	
	public Movie(int y, int d, double p, String t, Director ddir){
		year = y;
		duration = d;
		price = p;
		title = t;
		dir = ddir;
	}
	
	public Movie(Movie m){
		year = m.getYear();
		price = m.getPrice();
		duration = m.getDuration();
		title = m.getTitle();
		dir = new Director(m.getDirector());
	}
	/*public Movie(Movie m){
		setTitle(m.getTitle());
		setPrice(m.getPrice());
		setDuration(m.getDuration());
		setYear(m.getYear());
		setDirector((m.getDirector()).getFirst(), (m.getDirector()).getLast(), (m.getDirector()).getDob(), (m.getDirector()).getfilmsDir());
	}*/
	
	public String toString(){
		return "Title: " + title + "\nPublished in: " + year + "\nDuration of movie: " + duration + " minutes " +
				"\nPrice: $" + price + "\nDirected by " + dir.getFirst() + " " + dir.getLast() + ", who was born in " 
				+ dir.getDob() + " and has " + dir.getfilmsDir() + " releases.";
	}
	public void setTitle( String s){
		title = s;
	}
	
	public void setPrice ( double p){
		price = p;
	}
	
	public void setDuration( int d){
		duration = d;
	}
	
	public void setYear(int y){
		year = y;
	}
	
	public void setDirector( String f, String l, int d, int fD){
		dir = new Director(f, l, d ,fD);
	}
	
	public String getTitle(){
		return this.title;
	}
	
	public double getPrice(){
		return this.price;
	}
	
	public int getYear(){
		return this.year;
	}
	
	public int getDuration(){
		return this.duration;
	}
	
	public Director getDirector(){
		return this.dir;
	}
}


