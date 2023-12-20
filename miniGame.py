import numpy as np
import random
import pygame
import sys
import math
import game
import resources as res

rows = 6
columns = 7

player = 0
computer = 1

emptySurface = 0
playerPiece = 1
comPiece = 2

winLength = 4

sizeOfSquare = 100

width = columns * sizeOfSquare
height = (rows + 1) * sizeOfSquare

radius = int(sizeOfSquare / 2 - 5)

turn = random.randint(player, computer)

def createGameBoard():
    board = np.zeros((rows, columns))
    return board


def pieceDrop(board, row, col, piece):
    board[row][col] = piece


def validPlace(board, col):
    return board[rows - 1][col] == 0


def nextRow(board, col):
    for i in range(rows):
        if board[i][col] == 0:
            return i

def winMove(board, piece):
    # Check horizontal locations for win
    for i in range(columns - 3):
        for j in range(rows):
            if board[j][i] == piece and board[j][i + 1] == piece and board[j][i + 2] == piece and board[j][
                i + 3] == piece:
                return True

    # Check vertical locations for win
    for i in range(columns):
        for j in range(rows - 3):
            if board[j][i] == piece and board[j + 1][i] == piece and board[j + 2][i] == piece and board[j + 3][
                i] == piece:
                return True

    # Check positively sloped diaganols
    for i in range(columns - 3):
        for j in range(rows - 3):
            if board[j][i] == piece and board[j + 1][i + 1] == piece and board[j + 2][i + 2] == piece and board[j + 3][
                i + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for i in range(columns - 3):
        for j in range(3, rows):
            if board[j][i] == piece and board[j - 1][i + 1] == piece and board[j - 2][i + 2] == piece and board[j - 3][
                i + 3] == piece:
                return True


def winEvaluation(window, piece):
    score = 0
    oppPiece = playerPiece
    if piece == playerPiece:
        oppPiece = comPiece

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(emptySurface) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(emptySurface) == 2:
        score += 2

    if window.count(oppPiece) == 3 and window.count(emptySurface) == 1:
        score -= 4

    return score


def scorePos(board, piece):
    score = 0

    ## Score center column
    arrayCenter = [int(i) for i in list(board[:, columns // 2])]
    centerCount = arrayCenter.count(piece)
    score += centerCount * 3

    ## Score Horizontal
    for i in range(rows):
        rowArray = [int(x) for x in list(board[i, :])]
        for j in range(columns - 3):
            window = rowArray[j:j + winLength]
            score += winEvaluation(window, piece)

    ## Score Vertical
    for i in range(columns):
        colArray = [int(x) for x in list(board[:, i])]
        for j in range(rows - 3):
            window = colArray[j:j + winLength]
            score += winEvaluation(window, piece)

    ## Score posiive sloped diagonal
    for i in range(rows - 3):
        for j in range(columns - 3):
            window = [board[i + x][j + x] for x in range(winLength)]
            score += winEvaluation(window, piece)

    for i in range(rows - 3):
        for j in range(columns - 3):
            window = [board[i + 3 - x][j + x] for x in range(winLength)]
            score += winEvaluation(window, piece)

    return score


def isFinalNode(board):
    return winMove(board, playerPiece) or winMove(board, comPiece) or len(getValidLocations(board)) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    validLocations = getValidLocations(board)
    isFinal = isFinalNode(board)
    if depth == 0 or isFinal:
        if isFinal:
            if winMove(board, comPiece):
                return None, 100000000000000
            elif winMove(board, playerPiece):
                return None, -10000000000000
            else:  # Game is over, no more valid moves
                return None, 0
        else:  # Depth is zero
            return None, scorePos(board, comPiece)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = nextRow(board, col)
            boardCopy = board.copy()
            pieceDrop(boardCopy, row, col, comPiece)
            newScore = minimax(boardCopy, depth - 1, alpha, beta, False)[1]
            if newScore > value:
                value = newScore
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = nextRow(board, col)
            boardCopy = board.copy()
            pieceDrop(boardCopy, row, col, playerPiece)
            newScore = minimax(boardCopy, depth - 1, alpha, beta, True)[1]
            if newScore < value:
                value = newScore
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def getValidLocations(board):
    validLocations = []
    for col in range(columns):
        if validPlace(board, col):
            validLocations.append(col)
    return validLocations


def bestMove(board, piece):
    validLocations = getValidLocations(board)
    bestScore = -10000
    colBest = random.choice(validLocations)
    for col in validLocations:
        row = nextRow(board, col)
        temporaryBoard = board.copy()
        pieceDrop(temporaryBoard, row, col, piece)
        score = scorePos(temporaryBoard, piece)
        if score > bestScore:
            bestScore = score
            colBest = col

    return colBest


def drawBoard(board):
    for i in range(columns):
        for j in range(rows):
            pygame.draw.rect(game.screen, res.blue, (i * sizeOfSquare, j * sizeOfSquare + sizeOfSquare, sizeOfSquare, sizeOfSquare))
            pygame.draw.circle(game.screen, res.black, (
            int(i * sizeOfSquare + sizeOfSquare / 2), int(j * sizeOfSquare + sizeOfSquare + sizeOfSquare / 2)), radius)

    for i in range(columns):
        for j in range(rows):
            if board[j][i] == playerPiece:
                pygame.draw.circle(game.screen, res.red, (
                int(i * sizeOfSquare + sizeOfSquare / 2), height - int(j * sizeOfSquare + sizeOfSquare / 2)), radius)
            elif board[j][i] == comPiece:
                pygame.draw.circle(game.screen, res.yellow, (
                int(i * sizeOfSquare + sizeOfSquare / 2), height - int(j * sizeOfSquare + sizeOfSquare / 2)), radius)
    pygame.display.update()


