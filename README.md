<p>Author: Dang Linh Anh</p>

<p><strong>Code repository</strong>:&nbsp;<a href="https://gitlab.com/eyeq.tech/">https://gitlab.com/eyeq.tech/ocr-fast-label-tool</a></p>

<p><strong>Branches</strong>:</p>

<ul>
	<li>Master</li>
</ul>

<p><strong>Dependencies</strong>:</p>

<ul>
	<li>OS: Ubuntu &gt;= 18 (Recommended)</li>
	<li>PyQt5</li>
	<li>Python 3</li>
</ul>

<p><em>Note</em>: When working with Vietnamese, this tool may not work properly in Windows because of some GUI-based conflicts in encoding and decoding texts.&nbsp;</p>

<p><strong>Deploy instructions</strong>:&nbsp;</p>

<ul style="list-style-type:square;">
	<li>
	<p>Step 1: Put your input cropped images (into words) named <code>crop_img</code> in the same folder with script files</p>
	</li>
	<li>
	<p>Step 2: (Optional) The pre-recognized result file named <code>rec_gt.txt</code> must be put at the same folder with script files</p>
	</li>
	<li>
	<p>Step 3: To execute the GUI:</p></li>

```
    usage: label_imgs.py [-h] [--prev-row PREV_ROW] [--num-examples NUM_EXAMPLES]
                     [--num-cols NUM_COLS]

    optional arguments:
      -h, --help            show this help message and exit
      --prev-row PREV_ROW   Previous working row. For resuming.
      --num-examples NUM_EXAMPLES
                            Number of examples will be loaded into the table.
      --num-cols NUM_COLS   Number of main columns.
```
	
	<li>
	<p>Step 4: Start labeling! Using&nbsp;<b>Enter key </b>is recommended&nbsp;to traverse quickly to the next text column</p>
	</li>
	<li>
	<p>Step 5: (Optional) [<strong>Need backup]&nbsp;</strong>To clear output files&nbsp;to get ready for a next labeling session:</p>
	</li>

```
    chmod +x clear_outputfile.sh
    bash clear_outputfile.sh
```
	
</ul>

<p><strong>Usage</strong>:</p>

<ul style="list-style-type:square;">
	<li>The tool is organized into 5 main columns.&nbsp;Each column contains 2 entries named&nbsp;<strong>Input</strong>&nbsp;and&nbsp;<strong>Label</strong>.</li>
	<li>Buttons:&nbsp;
	<ul>
		<li><strong>Submit:&nbsp;</strong>Save all labeled words into <code>output.txt</code>. Any texts which are different from the initially loaded ones would be saved into <code>output_diff.txt</code>. Duplicated submissions do not change the output file.</li>
		<li><strong>Clear:&nbsp;</strong>Clear all texts on the working board.</li>
	</ul>
	</li>
	<li>Status bar: Display location of current editing cell for easy tracking.</li>
</ul>

<p><strong>Other notes</strong>:</p>

<ul>
	<li>Do not use&nbsp;<strong>Tab key</strong>&nbsp;for all the time. Because when submitting, the tool makes a recent&nbsp;row at which&nbsp;<strong>Enter key</strong>&nbsp;is pressed as the current row for saving.</li>
	<li>The&nbsp;pre-recognized result is loaded into rows. The number of examples which are&nbsp;not actually loaded into the table is the remainder part of the calculation of <code>NUM_EXAMPLES/NUM_COLS</code>.</li>
</ul>

<p><strong>Happy labeling!</strong></p>

<p>&nbsp;</p>
