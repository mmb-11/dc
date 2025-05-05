# server

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

interface HotelServerInterface extends Remote {
    boolean bookRoom(String guestName, int roomNumber) throws RemoteException;
    boolean cancelBooking(String guestName, int roomNumber) throws RemoteException;
}

public class HotelServer extends UnicastRemoteObject implements HotelServerInterface {
    private final Map<Integer, String> roomBookings = new HashMap<>();

    public HotelServer() throws RemoteException {}

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (roomNumber < 1 || roomNumber > 10 || roomBookings.containsKey(roomNumber)) return false;
        roomBookings.put(roomNumber, guestName);
        return true;
    }

    @Override
    public synchronized boolean cancelBooking(String guestName, int roomNumber) throws RemoteException {
        return roomBookings.remove(roomNumber, guestName);
    }

    public static void main(String[] args) {
        try {
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("rmi://localhost/HotelServer", new HotelServer());
            System.out.println("HotelServer is running.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

# client

import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelServerInterface hotelServer = (HotelServerInterface) Naming.lookup("rmi://localhost/HotelServer");
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("1. Book Room | 2. Cancel Booking | 3. Exit");
                System.out.print("Enter choice: ");
                int choice = scanner.nextInt();
                if (choice == 3) break;

                System.out.print("Enter guest name: ");
                String guestName = scanner.next();

                if (choice == 1) {
                    System.out.print("Enter room number (1-10): ");
                    int roomNumber = scanner.nextInt();
                    System.out.println(hotelServer.bookRoom(guestName, roomNumber) ? "Room booked!" : "Booking failed.");
                } else if (choice == 2) {
                    System.out.print("Enter room number to cancel: ");
                    int roomNumber = scanner.nextInt();
                    System.out.println(hotelServer.cancelBooking(guestName, roomNumber) ? "Booking canceled!" : "Cancellation failed.");
                } else {
                    System.out.println("Invalid choice.");
                }
            }
            System.out.println("Goodbye!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
