import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Controller {
	@FXML
    private void handleLogin() throws Exception {
		Parent window2 = FXMLLoader.load(getClass().getResource("groupProjectDetails.fxml"));
		Stage listStage = new Stage();
		listStage.setScene(new Scene(window2));
		listStage.show();
	}
	
	@FXML
	private void handleAddProject() throws Exception {
		Parent window3 = FXMLLoader.load(getClass().getResource("addNewSubProject.fxml"));
		Stage addStage = new Stage();
		addStage.setScene(new Scene(window3));
		addStage.show();
	}
	
	@FXML
	private void handleCloseWindow() throws Exception {
		
	}
}
