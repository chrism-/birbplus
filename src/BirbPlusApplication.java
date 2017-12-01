import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;


public class BirbPlusApplication extends Application {
	
	public static void main(String[] args) {
        launch(args);
    }
	
	@Override
	public void start(Stage loginStage) throws Exception {
		Parent window1 = FXMLLoader.load(getClass().getResource("login.fxml"));
		
		loginStage.setScene(new Scene(window1));
		loginStage.setTitle("Login");
		loginStage.show();
	}

}
