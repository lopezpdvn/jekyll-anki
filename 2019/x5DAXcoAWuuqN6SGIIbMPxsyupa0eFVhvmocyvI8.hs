{-
   This is a
   multi-line
   comment.
-}

divideByTen :: Floating a => a -> a
divideByTen = (/10)

y = divideByTen 950
main = putStrLn (show y)
