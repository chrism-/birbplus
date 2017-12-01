import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Controller {
	@FXML
    private void handleLogin() throws Exception {
		Parent window2 = FXMLLoader.load(getClass().getResource("list.fxml"));
		Stage listStage = new Stage();
		listStage.setScene(new Scene(window2));
		listStage.show();
	}
}
