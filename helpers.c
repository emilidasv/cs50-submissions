#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmpimage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j =0; j < width; j++)
        {
            tmpimage[i][j] = image[i][j];
        }
    };

    for (int i = 0; i < height; i++)
    {
        for (int j =0; j < width; j++)
        {
            if( i == 0)
            {

                if (j == 0)
                {
                    // i is 0 and j is 0  left top corner
                        int tmpblue=
                        tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue+
                        tmpimage[i + 1][j].rgbtBlue+ tmpimage[i + 1][j + 1].rgbtBlue;

                        tmpblue = round(tmpblue / 4.0);

                        int tmpgreen =
                        tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen+
                        tmpimage[i + 1][j].rgbtGreen+ tmpimage[i + 1][j + 1].rgbtGreen;

                        tmpgreen = round(tmpgreen / 4.0);

                        int tmpred =
                        tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed+
                        tmpimage[i + 1][j].rgbtRed+ tmpimage[i + 1][j + 1].rgbtRed;

                        tmpred = round(tmpred / 4.0);

                image[i][j].rgbtBlue = tmpblue;
                image[i][j].rgbtGreen = tmpgreen;
                image[i][j].rgbtRed = tmpred;


                }
                else if (j > 0 && j < width - 1)
                {
                // i is 0 and j is between 1 and width -2, top row, in middle
                        int tmpblue=
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue+
                        tmpimage[i+1][j - 1].rgbtBlue + tmpimage[i + 1][j].rgbtBlue+ tmpimage[i + 1][j + 1].rgbtBlue;

                        tmpblue = round(tmpblue / 6.0);

                        int tmpgreen =
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen+
                        tmpimage[i+1][j - 1].rgbtGreen + tmpimage[i + 1][j].rgbtGreen+ tmpimage[i + 1][j + 1].rgbtGreen;

                        tmpgreen = round(tmpgreen / 6.0);

                        int tmpred =
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed+
                        tmpimage[i+1][j - 1].rgbtRed + tmpimage[i + 1][j].rgbtRed+ tmpimage[i + 1][j + 1].rgbtRed;

                        tmpred = round(tmpred / 6.0);

                image[i][j].rgbtBlue = tmpblue;
                image[i][j].rgbtGreen = tmpgreen;
                image[i][j].rgbtRed = tmpred;

                }
                else if (j == width - 1)
                {
                // i is 0 and j is width - 1  ; top row left side
                        int tmpblue=
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue +
                        tmpimage[i+1][j - 1].rgbtBlue + tmpimage[i + 1][j].rgbtBlue;

                        tmpblue = round(tmpblue / 4.0);

                        int tmpgreen =
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen +
                        tmpimage[i+1][j - 1].rgbtGreen + tmpimage[i + 1][j].rgbtGreen;

                        tmpgreen = round(tmpgreen / 4.0);

                        int tmpred =
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed +
                        tmpimage[i+1][j - 1].rgbtRed + tmpimage[i + 1][j].rgbtRed;

                        tmpred = round(tmpred / 4.0);

                image[i][j].rgbtBlue = tmpblue;
                image[i][j].rgbtGreen = tmpgreen;
                image[i][j].rgbtRed = tmpred;



                }

            }
            else if ( i > 0 && i < height - 1)
            {
                if (j == 0)
                {
                                        // i > 0 and j = 0   , not top row , left side
                        int tmpblue=
                        tmpimage[i - 1][j].rgbtBlue + tmpimage[i - 1][j + 1].rgbtBlue+
                        tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue+
                        tmpimage[i + 1][j].rgbtBlue+ tmpimage[i + 1][j + 1].rgbtBlue;


                        tmpblue = round(tmpblue / 6.0);

                        int tmpgreen =
                        tmpimage[i - 1][j].rgbtGreen + tmpimage[i - 1][j + 1].rgbtGreen+
                        tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen+
                        tmpimage[i + 1][j].rgbtGreen+ tmpimage[i + 1][j + 1].rgbtGreen;

                        tmpgreen = round(tmpgreen / 6.0);

                        int tmpred =
                        tmpimage[i - 1][j].rgbtRed + tmpimage[i - 1][j + 1].rgbtRed+
                        tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed+
                        tmpimage[i + 1][j].rgbtRed+ tmpimage[i + 1][j + 1].rgbtRed;

                        tmpred = round(tmpred / 6.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }
                else if (j > 0 && j < width - 1)
                {
                    // i >0 and j < width - 2 not top row, middle
                        int tmpblue=
                        tmpimage[i - 1][j - 1].rgbtBlue + tmpimage[i - 1][j].rgbtBlue + tmpimage[i - 1][j + 1].rgbtBlue+
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue+
                        tmpimage[i+1][j - 1].rgbtBlue + tmpimage[i + 1][j].rgbtBlue+ tmpimage[i + 1][j + 1].rgbtBlue;

                        tmpblue = round(tmpblue / 9.0);

                        int tmpgreen =
                        tmpimage[i - 1][j - 1].rgbtGreen + tmpimage[i - 1][j].rgbtGreen + tmpimage[i - 1][j + 1].rgbtGreen+
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen+
                        tmpimage[i+1][j - 1].rgbtGreen + tmpimage[i + 1][j].rgbtGreen+ tmpimage[i + 1][j + 1].rgbtGreen;

                        tmpgreen = round(tmpgreen / 9.0);

                        int tmpred =
                        tmpimage[i - 1][j - 1].rgbtRed + tmpimage[i - 1][j].rgbtRed + tmpimage[i - 1][j + 1].rgbtRed+
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed+
                        tmpimage[i+1][j - 1].rgbtRed + tmpimage[i + 1][j].rgbtRed+ tmpimage[i + 1][j + 1].rgbtRed;

                        tmpred = round(tmpred / 9.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }
                else if (j == width - 1)
                {
                        // i >1 and j = width -1  ; not top row , last column
                        int tmpblue=
                        tmpimage[i - 1][j - 1].rgbtBlue + tmpimage[i - 1][j].rgbtBlue +
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue +
                        tmpimage[i+1][j - 1].rgbtBlue + tmpimage[i + 1][j].rgbtBlue;

                        tmpblue = round(tmpblue / 6.0);

                        int tmpgreen =
                        tmpimage[i - 1][j - 1].rgbtGreen + tmpimage[i - 1][j].rgbtGreen +
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen +
                        tmpimage[i+1][j - 1].rgbtGreen + tmpimage[i + 1][j].rgbtGreen;

                        tmpgreen = round(tmpgreen / 6.0);

                        int tmpred =
                        tmpimage[i - 1][j - 1].rgbtRed + tmpimage[i - 1][j].rgbtRed +
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed +
                        tmpimage[i+1][j - 1].rgbtRed + tmpimage[i + 1][j].rgbtRed;

                        tmpred = round(tmpred / 6.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }

            }

            else if ( i == height - 1)
            {
                if (j ==0)
                {
                    // i = last row  height - 1, j = first column  last row, first column
                        int tmpblue=
                        tmpimage[i - 1][j].rgbtBlue + tmpimage[i - 1][j + 1].rgbtBlue+
                        tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue;


                        tmpblue = round(tmpblue / 4.0);

                        int tmpgreen =
                       tmpimage[i - 1][j].rgbtGreen + tmpimage[i - 1][j + 1].rgbtGreen+
                        tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen;


                        tmpgreen = round(tmpgreen / 4.0);

                        int tmpred =
                         tmpimage[i - 1][j].rgbtRed + tmpimage[i - 1][j + 1].rgbtRed+
                         tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed;


                        tmpred = round(tmpred / 4.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }
                else if (j > 0 && j < width - 1)
                {
                    // i = last row j <> first or last column   last row, middle
                        int tmpblue=
                        tmpimage[i - 1][j - 1].rgbtBlue + tmpimage[i - 1][j].rgbtBlue + tmpimage[i - 1][j + 1].rgbtBlue+
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue + tmpimage[i][j + 1].rgbtBlue;


                        tmpblue = round(tmpblue / 6.0);

                        int tmpgreen =
                        tmpimage[i - 1][j - 1].rgbtGreen + tmpimage[i - 1][j].rgbtGreen + tmpimage[i - 1][j + 1].rgbtGreen+
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen + tmpimage[i][j + 1].rgbtGreen;


                        tmpgreen = round(tmpgreen / 6.0);

                        int tmpred =
                        tmpimage[i - 1][j - 1].rgbtRed + tmpimage[i - 1][j].rgbtRed + tmpimage[i - 1][j + 1].rgbtRed+
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed + tmpimage[i][j + 1].rgbtRed;


                        tmpred = round(tmpred / 6.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }
                else if (j == width - 1)
                {
                     // i = last row j , last column
                                            int tmpblue=
                        tmpimage[i - 1][j - 1].rgbtBlue + tmpimage[i - 1][j].rgbtBlue +
                        tmpimage[i][j - 1].rgbtBlue + tmpimage[i][j].rgbtBlue ;

                        tmpblue = round(tmpblue / 4.0);

                        int tmpgreen =
                        tmpimage[i - 1][j - 1].rgbtGreen + tmpimage[i - 1][j].rgbtGreen +
                        tmpimage[i][j - 1].rgbtGreen + tmpimage[i][j].rgbtGreen ;


                        tmpgreen = round(tmpgreen / 4.0);

                        int tmpred =
                        tmpimage[i - 1][j - 1].rgbtRed + tmpimage[i - 1][j].rgbtRed +
                        tmpimage[i][j - 1].rgbtRed + tmpimage[i][j].rgbtRed ;

                        tmpred = round(tmpred / 4.0);

                        image[i][j].rgbtBlue = tmpblue;
                        image[i][j].rgbtGreen = tmpgreen;
                        image[i][j].rgbtRed = tmpred;


                }

            };


        }
    }





    return;
}


// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
