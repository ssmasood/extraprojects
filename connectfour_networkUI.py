import I32CFSP
import connectfour_console
import connectfour
from collections import namedtuple

def game():
        try:
                host = input("Please enter the host: ")
                port = input("Please enter the port: ")
                user_name = input("Please enter Username: ")

                game_state = connectfour.new_game_state()
                the_connection = connect(host,port)
                login(the_connection, user_name)
        except:
                print("Invalid host/port")

        else:
                while connectfour.winning_player(game_state) == connectfour.NONE:
            
                        try:
                        
                                print("[ This is "+'['+"R"+']'+" player's turn ]")
                                print()
                                drop_pop = connectfour_console.drop_input()
                                column_number = input("Which column do you want to drop on? 1-7")
                                print()                
                                connectfour_console.valid(game_state,drop_pop)
                                game_state = connectfour_console.pop_n_drop(game_state, drop_pop,column_number)
                        except:
                                print('Please enter drop or pop and a column number from 1 - 7')
                        else:
                                print("[ This is "+'['+"Y"+']'+" player's turn ]")
                                print()
                                print(
                                "THE SERVER'S RESPONSE:")
                                write_to_server = (drop_pop.upper() + ' ' + str(column_number))
                                server_response = I32CFSP.server_drop(the_connection, write_to_server)
                                if server_response == 'WINNER_RED':
                                        break
                                if server_response != 'READY': #Adresses the server invalid
                                        server_drop = server_response.split()[0]
                                        server_col = server_response.split()[1]
                                        game_state = connectfour_console.pop_n_drop(game_state, server_drop, server_col)

        finally:
                print('        - CONGRATULATIONS PLAYER: '+connectfour.winning_player(game_state))
                I32CFSP.socket_close(the_connection)
def connect(host,port):
    connection = I32CFSP.connect(host,int(port))
    return connection

def login(connection, username):
        '''writes IC32FSP HELLO and AI Game automatically to the server and prints out response'''
        I32CFSP.login(connection,username)
        I32CFSP.AI(connection)

    
if __name__ == '__main__':
    game()
            
    
