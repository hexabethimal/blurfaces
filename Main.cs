using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BlurFaces
{
    public partial class Main : Form
    {
        string pathToOutputDir;

        public Main()
        {
            InitializeComponent();
        }

        private void Btn_selectfolder_Click(object sender, EventArgs e)
        {
            label1.Focus();
            using (FolderBrowserDialog openFolderDialog = new FolderBrowserDialog())
            {
                openFolderDialog.RootFolder = Environment.SpecialFolder.Desktop;                

                if (openFolderDialog.ShowDialog() == DialogResult.OK)
                {
                    Txt_folder.Text = openFolderDialog.SelectedPath;
                    Txt_folder.SelectionStart = Txt_folder.Text.Length;
                    Txt_folder.SelectionLength = 0;
                    pathToOutputDir = openFolderDialog.SelectedPath + "\\blur";
                }
            }
        }

        private void Btn_selectimage_Click(object sender, EventArgs e)
        {
            label1.Focus();
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
                openFileDialog.Filter = "Image Files (*.png;*.jpg;*.jpeg)|*.png;*.jpg;*.jpeg";
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    Txt_file.Text = openFileDialog.FileName;
                    Txt_file.SelectionStart = Txt_file.Text.Length;
                    Txt_file.SelectionLength = 0;
                    pathToOutputDir = Directory.GetParent(openFileDialog.FileName).ToString() + "\\blur";                    
                }
            }
        }

        private void Btn_blurallimages_Click(object sender, EventArgs e)
        {
            label1.Focus();
            if (Radio_50all.Checked || Radio_100all.Checked)
            {
                if (Radio_50all.Checked)
                {
                    RunPythonScript("folder", Txt_folder.Text, "", "50");
                }
                else
                {
                    RunPythonScript("folder", Txt_folder.Text, "", "100");
                }
            }
        }

        private void Btn_blurimage_Click(object sender, EventArgs e)
        {
            label1.Focus();
            if (Radio_50.Checked || Radio_100.Checked)
            {
                if (Radio_50.Checked)
                {
                    RunPythonScript("file", "", Txt_file.Text, "50");
                }
                else
                {
                    RunPythonScript("file", "", Txt_file.Text, "100");
                }
            }            
        }

        private void RunPythonScript(string fileOrFolder, string folderPath, string filePath, string scaling)
        {
            string pathToPythonScript = @"C:\Python313\blurall.py";
            string pathToPythonExe = @"C:\Python313\python.exe";            

            Process process = new Process
            {
                EnableRaisingEvents = true,
                StartInfo = new ProcessStartInfo
                {
                    FileName = pathToPythonExe,
                    Arguments = pathToPythonScript + " \"" + fileOrFolder + "\"" + " \"" + folderPath + "\"" + " \"" + filePath + "\"" + " \"" + scaling + "\"",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                }
            };
            process.Exited += new EventHandler(Process_Exited);
            process.Start();
            process.WaitForExit();
        }

        private void Process_Exited(object sender, EventArgs e)
        {
            Process.Start(pathToOutputDir);
        }
    }
}
