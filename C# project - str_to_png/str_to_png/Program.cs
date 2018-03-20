using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Text;
using System.Drawing.Imaging;

/// "notepad.exe   this is NOT a homoglyph. ｔһⅰѕ Ꭵｓ ａ ｈоrnοɡⅼｙрｈ." "Lucida Console Regular.TTF" "Lucida Console Regular homoglyph_output.png"



namespace str_to_png
{
    class Program
    {
        static void Parse_args(string[] args, ref String i_sStr, ref String i_sFontPath, ref String i_sImagePath)
        {
            for (int i = 0; i < args.Length; i++)
            {
                Console.WriteLine("arg_{0}: {1}", i, args[i]);
            }

            if (1 > args.Length)
            {
                Console.WriteLine("usage: str_to_image.exe [string_to_convert default=test_string] [font_name OR path_to_Font_file default=GenericSansSerif] [path_to_output_image]");
                i_sStr = "test_string";
            }
            else
            {
                i_sStr = args[0];
            }

            if (2 > args.Length)
            {
                Console.WriteLine("empty font argument, using default font: GenericSansSerif");
                i_sFontPath = "GenericSansSerif";
            }
            else
            {
                i_sFontPath = args[1];
            }

            if (3 > args.Length)
            {
                Console.WriteLine("empty path_to_output_image argument, using default path: output\\%timestamp%.png");
                System.IO.Directory.CreateDirectory("output");
                i_sImagePath = string.Concat("output\\", DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss-fff"), ".png");
            }
            else
            {
                i_sImagePath = args[2];
            }
        }

        static int Main(string[] args)
        {
            try
            {
                String i_sStr = null, i_sFontPath = null, i_sImagePath = null;
                Parse_args(args, ref i_sStr, ref i_sFontPath, ref i_sImagePath);

                //Font font1 = new Font(FontFamily.GenericSansSerif, 12.0F, FontStyle.Bold);
                //DrawText("test_string_from_code", font1, System.Drawing.Color.Black, 999999999, "C:\\Users\\Nir Rosen\\Desktop\\test2.png");
                Font Seleted_font = null;
                FontFamily family = null;
                if (System.IO.File.Exists(i_sFontPath)) {
                    PrivateFontCollection privateFontCollection = null;
                    family = LoadFontFamily(i_sFontPath, out privateFontCollection);
                    Seleted_font = new Font(family, 20.0f);
                }
                else {
                    //Seleted_font = new Font(FontFamily.GenericSansSerif, 12.0F, FontStyle.Bold);
                    Seleted_font = new Font(i_sFontPath, 12.0F, FontStyle.Bold);
                }

                DrawText(i_sStr, Seleted_font, System.Drawing.Color.Black, 0, i_sImagePath);

                // clean-up:
                if (null != Seleted_font)
                    Seleted_font.Dispose();
                if (null != family)
                    family.Dispose();
            }

            catch (Exception ex)
            {
                Console.WriteLine("Error Occured: {0}", ex.Message);
                return 1;
            }
            return 0;
        }

        public static FontFamily LoadFontFamily(string fileName, out PrivateFontCollection fontCollection)
        {
            fontCollection = new PrivateFontCollection();
            fontCollection.AddFontFile(fileName);
            return fontCollection.Families[0];
        }


        /// <summary>
        /// Converting text to image (png).
        /// </summary>
        /// <param name="text">text to convert</param>
        /// <param name="font">Font to use</param>
        /// <param name="textColor">text color</param>
        /// <param name="maxWidth">max width of the image</param>
        /// <param name="path">path to save the image</param>
        public static void DrawText(String text, Font font, Color textColor, int maxWidth, String path)
        {
            //first, create a dummy bitmap just to get a graphics object
            Image img = new Bitmap(1, 1);
            Graphics drawing = Graphics.FromImage(img);
            //measure the string to see how big the image needs to be
            SizeF textSize = drawing.MeasureString(text, font, maxWidth);

            //set the stringformat flags to rtl
            StringFormat sf = new StringFormat();
            //uncomment the next line for right to left languages
            //sf.FormatFlags = StringFormatFlags.DirectionRightToLeft;
            sf.Trimming = StringTrimming.Word;
            //free up the dummy image and old graphics object
            img.Dispose();
            drawing.Dispose();

            //create a new image of the right size
            img = new Bitmap((int)textSize.Width, (int)textSize.Height);

            drawing = Graphics.FromImage(img);
            //Adjust for high quality
            drawing.CompositingQuality = CompositingQuality.HighQuality;
            drawing.InterpolationMode = InterpolationMode.HighQualityBilinear;
            drawing.PixelOffsetMode = PixelOffsetMode.HighQuality;
            drawing.SmoothingMode = SmoothingMode.HighQuality;
            drawing.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            //paint the background
            //drawing.Clear(Color.Transparent);
            drawing.Clear(Color.White);

            //create a brush for the text
            Brush textBrush = new SolidBrush(textColor);

            drawing.DrawString(text, font, textBrush, new RectangleF(0, 0, textSize.Width, textSize.Height), sf);

            drawing.Save();

            textBrush.Dispose();
            drawing.Dispose();
            img.Save(path, ImageFormat.Png);
            img.Dispose();

        }


    }
}
