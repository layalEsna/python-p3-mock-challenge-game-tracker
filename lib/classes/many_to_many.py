# class Game:
#     game_results = []
#     def __init__(self, title, id = None):
#         self.title = title
#         self.id = id
#     @property
#     def title(self):
#         return self._title 
#     @title.setter
#     def title(self, title):
#         if not hasattr(self,'_title'):
#              if isinstance(title, str) and len(title) > 0:
#               self._title = title
#              else:
#                raise ValueError('Title must be a non-empty string.')
             
#         Game.game_results.append(self)

#     def results(self):
#         resu = []
#         for result in Game.game_results:
#           if isinstance(result, Result) and result.game == self:
#             resu.append(result)
#         return resu


    

#     def players(self):
#         players = []
#         for result in Game.game_results:
#             if isinstance(result, Result) and result.game == self:
#                 if isinstance(result.player, Player) and result.player not in players:
#                     players.append(result.player)
#         return players



#     def average_score(self, player):
#         if not isinstance(player, Player):
#             raise ValueError('player must be an instance of Player.')
#         total = 0
#         count = 0
#         for result in Game.game_results:
#             if isinstance(result, Result) and result.game == self and result.player == player:
#                 total += player.score
#                 count += 1
#         return total / count if count > 0 else None       



# class Player:
#     all_results = []
    
#     def __init__(self, username, id=None):
#         self.id = id
#         self.username = username  
    

#     @property
#     def username(self):
#         return self._username

#     @username.setter
#     def username(self, username):
#         if isinstance(username, str) and 2 <= len(username) <= 16:
#             self._username = username
#         else:
#             raise ValueError('Username must be a string and between 2 and 16 characters, inclusive.')

        
#     def results(self):
#         player_results = []  
#         for result in Player.all_results:
#             if isinstance(result, Result): 
#                 if result.player == self:   
#                     player_results.append(result)  

#         return player_results 
     
#     def games_played(self):
#         games = []
#         for result in Player.all_results:
#             if isinstance(result, Result) and result.player == self:
#                 if result.game not in games:
#                  games.append(result.game)
#         return games
        

#     def played_game(self, game):
#         for result in Player.all_results:
#             if isinstance(result, Result):
#                 if result.player == self and result.game == game:
#                     return True
            
#         return False



#     def num_times_played(self, game):
#        count = 0
#        for result in Player.all_results:
#            if isinstance(result, Result) and result.player == self and result.game == game:
              
#                 count += 1
#        return count

               


# class Result:
#     def __init__(self, player, game, score):
#         if not isinstance(player, Player):
#             raise ValueError('player must be an instance of Player.')
#         if not isinstance(game, Game):
#             raise ValueError('game must be an instance of Game.')
        
        
       
       

#         self._player = player
#         self._game = game
#         self._score = None
#         self.score = score
     

#     @property
#     def player(self):
#             return self._player
        
#     @property
#     def game(self):
#             return self._game
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     @score.setter
#     def score(self, score):
#         # Ensure score is only set once, and cannot be changed later
#         if self._score is not None:
#             raise AttributeError('Cannot change the score after it has been set.')
#         if isinstance(score, int) and 1 <= score <= 5000:
#             self._score = score
#         else:
#             raise ValueError('Score must be an integer between 1 and 5000.')







class Game:
    game_results = []

    def __init__(self, title, id=None):
        self.title = title
        self.id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title, str) and len(title) > 0:
                self._title = title
            else:
                raise ValueError('Title must be a non-empty string.')
        Game.game_results.append(self)

    def results(self):
        resu = []
        for result in Game.game_results:
            if isinstance(result, Result) and result.game == self:
                resu.append(result)
        return resu

    def players(self):
        players = []
        for result in Game.game_results:
            if isinstance(result, Result) and result.game == self:
                if isinstance(result.player, Player) and result.player not in players:
                    players.append(result.player)
        return players

    def average_score(self, player):
        if not isinstance(player, Player):
            raise ValueError('player must be an instance of Player.')
        total = 0
        count = 0
        for result in Game.game_results:
            if isinstance(result, Result) and result.game == self and result.player == player:
                total += result.score  # Corrected to use result.score
                count += 1
        return total / count if count > 0 else None


class Player:
    all_results = []

    def __init__(self, username, id=None):
        self.id = id
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError('Username must be a string and between 2 and 16 characters, inclusive.')

    def results(self):
        player_results = []
        for result in Player.all_results:
            if isinstance(result, Result):
                if result.player == self:
                    player_results.append(result)
        return player_results

    def games_played(self):
        games = []
        for result in Player.all_results:
            if isinstance(result, Result) and result.player == self:
                if result.game not in games:
                    games.append(result.game)
        return games

    def played_game(self, game):
        for result in Player.all_results:
            if isinstance(result, Result):
                if result.player == self and result.game == game:
                    return True
        return False

    def num_times_played(self, game):
        count = 0
        for result in Player.all_results:
            if isinstance(result, Result) and result.player == self and result.game == game:
                count += 1
        return count


class Result:
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise ValueError('player must be an instance of Player.')
        if not isinstance(game, Game):
            raise ValueError('game must be an instance of Game.')

        self._player = player
        self._game = game
        self._score = None  # Initializing score as None
        self.score = score  # Score is set here using the setter

        # Add to Player.all_results and Game.game_results lists
        Player.all_results.append(self)
        Game.game_results.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        # Ensure score is only set once, and cannot be changed later
        if self._score is not None:
            raise AttributeError('Cannot change the score after it has been set.')
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise ValueError('Score must be an integer between 1 and 5000.')
        
        # second try
        

