import java.util.ArrayList;
import java.util.Iterator;

public class Team {

	ArrayList<FreeLancer> freeLancers = new ArrayList<FreeLancer>();
	
	public Team(){
		
	}
	
	public void addMember(FreeLancer f){
		Iterator<FreeLancer> i = freeLancers.iterator();
		boolean alreadyAdded = false;
		
		
		while(i.hasNext()){
			
			if(i.next().getId() == f.getId()){
				alreadyAdded = true;
			}
			
		}
		
		if(!alreadyAdded){
			freeLancers.add(f);
		}
	}
	
	public void removeMember(FreeLancer f){
		
		freeLancers.remove(f);
		
	}
	
}
