import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.Scanner;

public class CS3380A3Q3 {
    static Connection connection;

    public static void main(String[] args) throws Exception {
        // Startup sequence
        MyDatabase db = new MyDatabase();
        runConsole(db);

        System.out.println("Exiting...");
    }

    public static void runConsole(MyDatabase db) {
        Scanner console = new Scanner(System.in);
        System.out.print("Welcome! Type h for help. ");
        System.out.print("db > ");
        String line = console.nextLine();
        String[] parts;
        String arg = "";

        while (line != null && !line.equals("q")) {
            parts = line.split("\\s+");
            if (line.indexOf(" ") > 0)
                arg = line.substring(line.indexOf(" ")).trim();

            if (parts[0].equals("h")) {
                printHelp();
            } else if (parts[0].equals("mp")) {
                db.getMostPublishers();
            } else if (parts[0].equals("s")) {
                if (parts.length >= 2) db.nameSearch(arg);
                else System.out.println("Require an argument for this command");
            } else if (parts[0].equals("l")) {
                try {
                    if (parts.length >= 2) db.lookupByID(arg);
                    else System.out.println("Require an argument for this command");
                } catch (Exception e) {
                    System.out.println("id must be an integer");
                }
            } else if (parts[0].equals("sell")) {
                try {
                    if (parts.length >= 2) db.lookupWhoSells(arg);
                    else System.out.println("Require an argument for this command");
                } catch (Exception e) {
                    System.out.println("id must be an integer");
                }
            } else if (parts[0].equals("notsell")) {
                try {
                    if (parts.length >= 2) db.whoDoesNotSell(arg);
                    else System.out.println("Require an argument for this command");
                } catch (Exception e) {
                    System.out.println("id must be an integer");
                }
            } else if (parts[0].equals("mc")) {
                db.mostCities();
            } else if (parts[0].equals("notread")) {
                db.ownBooks();
            } else if (parts[0].equals("all")) {
                db.readAll();
            } else if (parts[0].equals("mr")) {
                db.mostReadPerCountry();
            } else {
                System.out.println("Read the help with h, or find help somewhere else.");
            }

            System.out.print("db > ");
            line = console.nextLine();
        }
        console.close();
    }

    private static void printHelp() {
        System.out.println("Library database");
        System.out.println("Commands:");
        System.out.println("h - Get help");
        System.out.println("s <name> - Search for a name");
        System.out.println("l <id> - Search for a user by id");
        System.out.println("sell <author id> - Search for stores that sell books by this author");
        System.out.println("notread - Books not read by its own author");
        System.out.println("all - Authors that have read all their own books");
        System.out.println("notsell <author id> - List of stores that do not sell this author");
        System.out.println("mp - Authors with the most publishers");
        System.out.println("mc - Authors with books in the most cities");
        System.out.println("mr - Most read book by country");
        System.out.println("");
        System.out.println("q - Exit the program");
        System.out.println("---- end help ----- ");
    }
}

class MyDatabase {
    private Connection connection;

    public MyDatabase() {
        try {
            String url = "jdbc:sqlite:library.db";
            connection = DriverManager.getConnection(url);
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 1. Search for a person by a partial name match
    public void nameSearch(String name) {
        String query = "SELECT first, last, id FROM people WHERE LOWER(first) LIKE LOWER(?) OR LOWER(last) LIKE LOWER(?)";
        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            pstmt.setString(1, "%" + name + "%");
            pstmt.setString(2, "%" + name + "%");
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                System.out.println("First Name: " + rs.getString("first") + ", Last Name: " + rs.getString("last") + ", ID: " + rs.getInt("id"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 2. Lookup a person by ID and report their Author ID if available
    public void lookupByID(String id) {
        String query = "SELECT first, last, COALESCE(aid, 'No Author ID') AS author_id FROM people WHERE id = ?";
        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            pstmt.setInt(1, Integer.parseInt(id));
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                System.out.println("First Name: " + rs.getString("first") + ", Last Name: " + rs.getString("last") + ", Author ID: " + rs.getString("author_id"));
            } else {
                System.out.println("No person found with that ID.");
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 3. Find stores that sell books by a particular author ID
    public void lookupWhoSells(String id) {
        String query = "SELECT store.name, COUNT(books.bid) AS books_on_sale " +
                       "FROM store " +
                       "JOIN sells ON store.id = sells.sid " +
                       "JOIN books ON sells.pid = books.pid " +
                       "WHERE books.aid = ? " +
                       "GROUP BY store.name";
        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            pstmt.setInt(1, Integer.parseInt(id));
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                System.out.println("Store: " + rs.getString("name") + ", Books on Sale: " + rs.getInt("books_on_sale"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 4. List books that have not been read by their own authors
    public void ownBooks() {
        String query = "SELECT people.first || ' ' || people.last AS author_name, books.title AS book_title FROM books JOIN people ON books.aid = people.id LEFT JOIN read ON read.bid = books.bid AND read.id = people.id WHERE read.bid IS NULL";
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Author: " + rs.getString("author_name") + ", Book Title: " + rs.getString("book_title"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 5. Find authors who have read all their own books
    public void readAll() {
        String query = "SELECT DISTINCT people.first || ' ' || people.last AS name FROM people WHERE NOT EXISTS (SELECT 1 FROM books WHERE books.aid = people.id AND books.bid NOT IN (SELECT bid FROM read WHERE id = people.id))";
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Author: " + rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 6. List stores that do not sell books by a certain author
    public void whoDoesNotSell(String id) {
        String query = "SELECT store.name " +
                       "FROM store " +
                       "WHERE store.id NOT IN (" +
                       "    SELECT sells.sid " +
                       "    FROM sells " +
                       "    JOIN books ON sells.pid = books.pid " +
                       "    WHERE books.aid = ?" +
                       ")";
        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            pstmt.setInt(1, Integer.parseInt(id));
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                System.out.println("Store: " + rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 7. Find the top 5 authors with the most publishers
    public void getMostPublishers() {
        String query = "SELECT people.first, people.last, COUNT(DISTINCT publishers.pid) AS publisher_count FROM people JOIN books ON people.id = books.aid JOIN publishers ON books.pid = publishers.pid GROUP BY people.id ORDER BY publisher_count DESC LIMIT 5";
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Author: " + rs.getString("first") + " " + rs.getString("last") + ", Publishers: " + rs.getInt("publisher_count"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 8. Find the top 5 authors whose books are sold in the most cities
    public void mostCities() {
        String query = "SELECT people.first || ' ' || people.last AS name, COUNT(DISTINCT city.name) AS cities_count " +
                       "FROM people " +
                       "JOIN books ON people.id = books.aid " +
                       "JOIN sells ON books.pid = sells.pid " +
                       "JOIN store ON sells.sid = store.id " +
                       "JOIN city ON store.cid = city.cid " +
                       "GROUP BY people.id " +
                       "ORDER BY cities_count DESC " +
                       "LIMIT 5";
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Author: " + rs.getString("name") + ", Cities: " + rs.getInt("cities_count"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }

    // 9. Find the most-read book in each country
    public void mostReadPerCountry() {
        String query = "SELECT country, title FROM (" +
                       "    SELECT city.country AS country, books.title AS title, COUNT(read.bid) AS read_count, " +
                       "           RANK() OVER (PARTITION BY city.country ORDER BY COUNT(read.bid) DESC) AS rank " +
                       "    FROM books " +
                       "    JOIN read ON read.bid = books.bid " +
                       "    JOIN sells ON books.pid = sells.pid " +
                       "    JOIN store ON sells.sid = store.id " +
                       "    JOIN city ON store.cid = city.cid " +
                       "    GROUP BY city.country, books.title " +
                       ") WHERE rank = 1";
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Country: " + rs.getString("country") + ", Most Read Book: " + rs.getString("title"));
            }
        } catch (SQLException e) {
            e.printStackTrace(System.out);
        }
    }
}
