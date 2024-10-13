import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.PreparedStatement;

public class CallTheManager {
	/**
	 * Connect to a sample database
	 */

	/**
	 * @param args the command line arguments
	 */
	public static void main(String[] args) {
		MyDatabase db = new MyDatabase("staff.sql");

		db.getStaffMember(20001);
		db.getStaffMember(10001);
		db.getStaffMember(1);
		db.getManager(1);
		db.getManager(10001);
		db.getManager(20001);
		db.getManager(10);

		System.out.println("Exiting...");
		db.shutdown();
	}
}

class MyDatabase {
	private Connection connection;

	public MyDatabase(String initScript) {
		connection = null;
		try {
			// db parameters
			String url = "jdbc:sqlite::memory:";
			// if you want persistence....
			// String url = "jdbc:sqlite:teaching.db";
			// create a connection to the database
			connection = DriverManager.getConnection(url);

			System.out.println("Connection to SQLite has been established.");

			if (initScript != null)
				this.loadData(initScript);

		} catch (SQLException e) {
			System.out.println(e.getMessage());
			System.exit(1);
		} catch (IOException fnf) {
			System.out.println(fnf.getMessage());
			System.exit(2);
		}

	}

	public void loadData(String script) throws IOException, SQLException {
		BufferedReader reader = new BufferedReader(new FileReader(script));
		String line = reader.readLine();
		// assumes each query is its own line
		while (line != null) {
			//System.out.println(line);
			this.connection.createStatement().execute(line);
			line = reader.readLine();
		}
	}

	public void shutdown() {
		try {
			connection.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public void showAll() {
		try {
			String sql = "Select * from staff;";

			Statement statement = connection.createStatement();
			ResultSet resultSet = statement.executeQuery(sql);

			while (resultSet.next()) {
				System.out.println(resultSet.getInt("id") + " - " + resultSet.getString("firstname") + " "
						+ resultSet.getString("lastname") + ", " + resultSet.getInt("manager"));

			}
			resultSet.close();
			statement.close();
		} catch (SQLException e) {
			e.printStackTrace(System.out);
		}
	}

	public void getStaffMember(int id) {
		try {
			String sql = "Select * from staff where id = ?";

			PreparedStatement statement = connection.prepareStatement(sql);
			statement.setInt(1, id);
			ResultSet resultSet = statement.executeQuery();

			System.out.println("Showing single staff member " + id);
			while (resultSet.next()) {
				if (resultSet.getString("manager") == null) // alternatively, check for 0. Neither feels satisfying
					System.out.println("The boss!");
				System.out.println(resultSet.getInt("id") + " - " + resultSet.getString("firstname") + " "
						+ resultSet.getString("lastname") + ", " + resultSet.getInt("manager"));

			}
			resultSet.close();
			statement.close();
		} catch (SQLException e) {
			e.printStackTrace(System.out);
		}

	}

	public void getManager(int id) {
		try {
			String sql = "SELECT id, firstname, lastname, manager FROM staff WHERE id = ?";
			PreparedStatement statement = connection.prepareStatement(sql);
			
			System.out.println("Getting manager path for " + id);
			
			int currentId = id;
			
			while (currentId != 0) {
				statement.setInt(1, currentId);
				ResultSet resultSet = statement.executeQuery();
				
				if (resultSet.next()) {
					int staffId = resultSet.getInt("id");
					String firstName = resultSet.getString("firstname");
					String lastName = resultSet.getString("lastname");
					Integer managerId = resultSet.getObject("manager") != null ? resultSet.getInt("manager") : null;
					
					// Print the current staff member's info
					System.out.println(staffId + " - " + firstName + " " + lastName + (managerId != null ? ", " + managerId : ", 0"));
					
					// Move to the manager
					if (managerId != null) {
						currentId = managerId;
					} else {
						break; // reached the top of the hierarchy
					}
				} else {
					System.out.println("No staff member found with ID " + currentId);
					break;
				}
				resultSet.close();
			}
			
			statement.close();
			
		} catch (SQLException e) {
			e.printStackTrace(System.out);
		}
	}
	

}