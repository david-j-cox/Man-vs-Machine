

# Install pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use pacman to load add-on packages as desired
pacman::p_load(pacman, rio) 

# Libraries we'll use throughout the script
library(dplyr)

# Read in the data Set
df <- import("C:/Users/David/Downloads//NBA Play by Play Data Toronto Raptors vs Utah Jazz.xlsx")
head(df) # Take a peek at the top few rows odof the df to see what we're working with 

# It looks like the time in seconds is per quarter and we want the total time remaining in the game
# so that can bin across quarters if needed. Let's add that column. 
quarter <- 4     # Four quarters in a game
game_time <- c() # Empty list to store new values

for (row in 1:nrow(df)){             # For each row in the df...
  time <- df[row, 'Time in seconds'] # ...get the value from the "Time in seconds" column...
  if(time == 720){                   # ...if that value is 720, we've started a new quarter...
    quarter <- quarter-1             # ...so let's subtract 1 from our quarter value...
    time_add <- quarter*720          # ...calculate how much time we want to add to the time in seconds column...
  }
  game_time <- append(game_time, time+time_add) # ...add the time we want to add to the time from the "Time in seconds" col, and append it to the empty list.
} 

# Add that overall game time column to our df
df$game_time <- game_time
save(df, file="NBA_Data.csv")  # Save the progress made


# Defining the bins we want to test:
# Rather than having to hand write out the intervals we want to test each time, we can 
# create a bin variable we want to use to create the list we'll iterate through. 
bin_width = 300           # 300 seconds which = 5 min *** THIS IS WHAT YOU CAN CHANGE TO GET NEW BIN WIDTHS
total_time = 720*4        # 720 seconds in a quarter times 4 quarters 
intervals = c(720*4)
while (total_time>0) {
  total_time <- total_time-bin_width
  if(total_time>0){
    intervals <- append(intervals, total_time)}
  else{
    intervals <- append(intervals, 0)
  }
}

# Now let's grab the count of the 2-pointers during those bins. 
two_pts_shot <- c()  # Initialize an empty list to store our shot counts
two_pts_made <- c()  # Initialize an empty list to store our shots made. 
sequence <- seq(1, (length(intervals)-1), 1)  # Create a list of numbers for us to use below

for(value in sequence) {  # We'll loop through the intervals list we created above to get our counts
  start_time <- intervals[value]       # Set the start of the time we want to slice
  end_time <- intervals[value+1]      # Set the end of the time we want to slice
  
  # Create the subset of the data frame using the start and end time
  subset_df <- df[(df$game_time<=start_time) & (df$game_time>end_time),]
  two_shots <- sum(subset_df$"TR 2PA")              # Count the number of 2-pointers attempted
  two_makes  <- sum(subset_df$"TR 2P")              # Count the number of 2-pointers attempted
  two_pts_shot <- append(two_pts_shot, two_shots)   # Append count of shots taken to the list above
  two_pts_made <- append(two_pts_made, two_makes)   # Append count of shots made to the list above
}

# You now have the data on the number of 2-point shots attempted using the 
# assigned bin width and the number of 2-point shots made for each of those bins.
two_pts_shot
two_pts_made

# All that is left is to:
#   (1) Do the same thing for the three point shots.
#   (2) Turn the above two-point lists and the three-point lists into a data frame. 
#   (3) Fit the matching equation to the new data frame. 
#   (4) Repeat the above across a bunch of bin widths to see if/when the bind width results in matching. 






'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Solution
interval <- c(720,690,660,630,600,570,540,510,480,450,420,390,360,300,270,240,210,180,150,120,90,60,30,0)

require(dplyr)

result<-dataTRvsUJ %>% 
  mutate(energybudget=(dataTRvsUJ$`TR Score`-dataTRvsUJ$`UJ Score`)) %>% 
        group_by(Quarter) %>% 
        mutate(thirtysecbin=cut(`Time in seconds`,interval)) %>% 
        group_by(thirtysecbin) %>% 
  Summarize(n())
       


randVec <- c()
for(i in 1:10){
  randNorm <- rnorm(1,0,1)
  randVec <- append(randVec,randNorm)
}
print(randVec)
