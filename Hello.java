import java.sql.*;

public class Hello {

    public static void main(String[] args) throws Exception {

        String username = "admin";

        Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/test",
                "root",
                "password"
        );

        Statement stmt = con.createStatement();

        // ❌ SQL Injection Vulnerability
        String query = "SELECT * FROM users WHERE username='" 
                        + username + "'";

        ResultSet rs = stmt.executeQuery(query);

        while(rs.next()) {
            System.out.println(rs.getString("username"));
        }

        con.close();
    }
}
