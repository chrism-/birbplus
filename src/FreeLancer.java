
public class FreeLancer {

	String name;
	int id;
	
	String skills;
	
	String description;
	double hireRate;
	
	public FreeLancer(String name, int id, String skills, String description, double hireRate) {
		super();
		this.name = name;
		this.id = id;
		this.skills = skills;
		this.description = description;
		this.hireRate = hireRate;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getSkills() {
		return skills;
	}

	public void setSkills(String skills) {
		this.skills = skills;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public double getHireRate() {
		return hireRate;
	}

	public void setHireRate(double hireRate) {
		this.hireRate = hireRate;
	}
	
	
	

	
}
