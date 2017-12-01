import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;


public class BirbPlusApplication extends Application {
	
	private static String USER_AGENT = "Mozilla/5.0";
	private static String POST_PARAM = "userName=";
	
	public static void main(String[] args) throws Exception {
		sendPost();
        launch(args);
    }
	
	// https://www.journaldev.com/7148/java-httpurlconnection-example-java-http-request-get-post
	public static void sendPost() throws Exception {
		URL url = new URL("https://www.freelancer-sandbox.com/api/");
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestMethod("POST");
		con.setRequestProperty("User-Agent", USER_AGENT);
		con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
		
		con.setDoOutput(true);
		OutputStream os = con.getOutputStream();
		os.write(POST_PARAM.getBytes());
		os.flush();
		os.close();
		
	}
	
	@Override
	public void start(Stage loginStage) throws Exception {
		Parent window1 = FXMLLoader.load(getClass().getResource("login.fxml"));
		
		loginStage.setScene(new Scene(window1));
		loginStage.setTitle("Login");
		loginStage.show();
	}

}
