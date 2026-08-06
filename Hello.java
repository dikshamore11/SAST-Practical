import java.sql.*;

public class Hello {

    public static void main(String[] args) throws Exception {


        String username = args[0];


        Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost/test",
                "root",
                "password"
        );


        Statement statement = con.createStatement();


        // VULNERABLE CODE
        String sql = "SELECT * FROM users WHERE name='" 
                     + username + "'";


        ResultSet result = statement.executeQuery(sql);


        while(result.next()) {
            System.out.println(result.getString(1));
        }

    }
}
