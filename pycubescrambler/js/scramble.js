"use strict";
var scramble = (function(rn, rndEl) {
	//var div = $('<div id="scrambleDiv"/>');
	//var title = $('<div />').addClass('title');
	//var select = $('<select />');
	//var select2 = $('<select />');
	//var scrLen = $('<input type="text" maxlength="3">');
	//var sdiv = $('<div id="scrambleTxt"/>');
	var alias = {
		'333fm': '333',
		'333oh': '333',
		'333ft': '333',
		'444bld': '444wca',
		'555bld': '555wca'
	};

	//var inputText = $('<textarea />');

	var inputScramble = [];

	function mega(turns, suffixes, length) {
		if (suffixes == undefined) {
			suffixes = [""];
		}
		if (length == undefined) {
			length = len;
		}
		var donemoves = 0;
		var lastaxis = -1;
		var s = [];
		var first, second;
		for (var i = 0; i < length; i++) {
			do {
				first = rn(turns.length);
				second = rn(turns[first].length);
				if (first != lastaxis) {
					donemoves = 0;
					lastaxis = first;
				}
			} while (((donemoves >> second) & 1) != 0);
			donemoves |= 1 << second;
			if (turns[first][second].constructor == Array) {
				s.push(rndEl(turns[first][second]) + rndEl(suffixes));
			} else {
				s.push(turns[first][second] + rndEl(suffixes));
			}
		}
		return s.join(' ');
	}

	// #################### SCRAMBLING ####################


	var type, lasttype, typeExIn = '333o';
	var len = 0;
	var cubesuff = ["", "2", "'"];
	var minxsuff = ["", "2", "'", "2'"];
	var scramble, lastscramble;

	function doScrambleIt() {
		calcScramble();
		if (scramble) {
			scrambleOK();
		} else {
			sdiv.html("Scramble Error. ");
		}
	}

	function calcScramble() {
		scramble = "";
		var realType = type;
		if (type in alias) {
			realType = alias[type];
		}

		if (realType in scramblers) {
			scramble = scramblers[realType](realType, len);
			return;
		}

		switch (realType) {
			case "input":
				if (inputScramble.length == 0) {
					inputText.val("");
					kernel.showDialog([inputText, inputOK, inputCancel], 'input', SCRAMBLE_INPUT);
					return;
				} else {
					scramble = inputScramble.shift();
				}
				break;
		}
	}

	function scrambleOK(scrStr) {
		scramble = (scrStr || scramble).replace(/(\s*)$/, "");
		sdiv.html(scramble);
		kernel.pushSignal('scramble', [type, scramble]);
	}

	function inputOK() {
		if (!parseInput(inputText.val())) {
			kernel.setProp('scrType', typeExIn);
		} else {
			doScrambleIt();
		}
	}

	function inputCancel() {
		kernel.setProp('scrType', typeExIn);
	}

	/**
	 *	{type: callback(type, length)}
	 *	callback return: scramble string or undefined means delay
	 */
	var scramblers = {};

	function regScrambler(type, callback) {
		// console.log(type);
		if (Array.isArray(type)) {
			for (var i = 0; i < type.length; i++) {
				scramblers[type[i]] = callback;
			}
		} else {
			scramblers[type] = callback;
		}
		return regScrambler;
	}

	/**
	function loadSelect2(idx) {
		if (!$.isNumeric(idx)) {
			idx = 0;
			var selectedStr = scrdata[select[0].selectedIndex][0];
			if (selectedStr && selectedStr.match(/^===/)) {
				select[0].selectedIndex++;
			}
		} else {
			kernel.blur();
		}
		var box2 = scrdata[select[0].selectedIndex][1];
		select2.empty();
		for (var i = 0; i < box2.length; i++) {
			select2.append('<option value="' + box2[i][1] + '">' + box2[i][0] + '</option');
		}
		select2[0].selectedIndex = idx;
		scrLen.val(Math.abs(box2[idx][2]));
		scrLen[0].disabled = box2[idx][2] <= 0;
		genScramble();
	}
	**/

	function getLastScramble() {
		return [lasttype, lastscramble];
	}

	function getCurScramble() {
		return [type, scramble];
	}

	function parseInput(str) {
		if (str.match(/^\s*$/)) {
			return false;
		}
		inputScramble = [];
		var inputs = str.split('\n');
		for (var i = 0; i < inputs.length; i++) {
			var s = inputs[i];
			if (s.match(/^\s*$/) == null) {
				inputScramble.push(s.replace(/^\d+[\.\),]\s*/, ''));
			}
		}
		return inputScramble.length != 0;
	}

	var isEn = false;

	function procSignal(signal, value) {
		if (signal == 'time') {
			if (isEn) {
				genScramble();
			} else {
				sdiv.empty();
				kernel.pushSignal('scramble', ['-', '']);
			}
		} else if (signal == 'property') {
			if (value[0] == 'scrSize') {
				sdiv.css('font-size', value[1] / 7 + 'em');
			} else if (value[0] == 'scrMono') {
				div.css('font-family', value[1] ? 'SimHei, Monospace' : 'Arial');
			} else if (value[0] == 'scrType') {
				if (value[1] != select2.val()) {
					loadType(value[1]);
				}
			} else if (value[0] == 'scrLim') {
				if (value[1]) {
					sdiv.addClass('limit');
				} else {
					sdiv.removeClass('limit');
				}
			} else if (value[0] == 'scrAlign') {
				if (value[1] == 'c') {
					div.css('text-align', 'center');
				} else if (value[1] == 'l') {
					div.css('text-align', 'left');
				} else if (value[1] == 'r') {
					div.css('text-align', 'right');
				}
			}
		} else if (signal == 'button' && value[0] == 'scramble') {
			isEn = value[1];
			if (isEn && sdiv.html() == '') {
				genScramble();
			}
		} else if (signal == 'ctrl' && value[0] == 'scramble') {
			if (value[1] == 'last') {
				sdiv.html(lastscramble);
			} else if (value[1] == 'next') {
				if (sdiv.html() == lastscramble) {
					sdiv.html(scramble);
				} else {
					genScramble();
				}
			}
		}
	}

	function loadType(type) {
		for (var i = 0; i < scrdata.length; i++) {
			for (var j = 0; j < scrdata[i][1].length; j++) {
				if (scrdata[i][1][j][1] == type) {
					select[0].selectedIndex = i;
					loadSelect2(j);
					return;
				}
			}
		}
	}

	var scrambleGenerator = (function() {

		function generate() {
			var n_scramble = ~~scrNum.val();
			var scrambles = "";
			var scramble_copy = scramble;
			var pre = prefix.val();
			for (var i = 0; i < n_scramble; i++) {
				calcScramble();
				scrambles += pre.replace('1', i + 1) + scramble + "\n";
			}
			// console.log(scrambles);
			scramble = scramble_copy;
			output.text(scrambles);
			output.select();
		}

		return function(fdiv) {
			if (!fdiv) {
				return;
			}
		}
	})();

	/**
	 *	format string, 
	 *		${args} => scramblers[scrType](scrType, scrArg)
	 *		#{args} => mega(args)
	 */
	function formatScramble(str,length,manuallyAssignLength,skipPassingSuffixes) {

		if (length === undefined){
			length = 25;
		}
		if (manuallyAssignLength === undefined){
			manuallyAssignLength = false;
		}

		if (skipPassingSuffixes === undefined){
			skipPassingSuffixes = false;
		}

		var repfunc = function(match, p1) {
			// console.log(match);
			if (match[0] == '$') {
				var args = [p1];
				if (p1[0] == '[') {
					args = JSON.parse(p1);
				}
				// console.log(args[0]);
				// console.log(scramblers[args[0]]);
				return scramblers[args[0]].apply(this, args);
			} else if (match[0] == '#') {
				var theArgs = JSON.parse('[' + p1 + ']');
				if (manuallyAssignLength)
				{
					if (skipPassingSuffixes){
						theArgs.push(undefined);
					}

					theArgs.push(length);
				}
				return mega.apply(this, theArgs);
			} else {
				return '';
			}
		};
		var re1 = /[$#]\{([^\}]+)\}/g;
		return str.replace(re1, repfunc);
	}

	/**
	$(function() {
		kernel.regListener('scramble', 'time', procSignal);
		kernel.regListener('scramble', 'property', procSignal, /^scr(?:Size|Mono|Type|Lim|Align)$/);
		kernel.regListener('scramble', 'button', procSignal, /^scramble$/);
		kernel.regListener('scramble', 'ctrl', procSignal, /^scramble$/);
		kernel.regProp('scramble', 'scrSize', 2, PROPERTY_SCRSIZE, [15, 5, 50]);
		kernel.regProp('scramble', 'scrMono', 0, PROPERTY_SCRMONO, [true]);
		kernel.regProp('scramble', 'scrLim', 0, PROPERTY_SCRLIM, [true]);
		kernel.regProp('scramble', 'scrAlign', 1, PROPERTY_SCRALIGN, ['c', ['c', 'l', 'r'], PROPERTY_SCRALIGN_STR.split('|')]);
		kernel.regProp('scramble', 'preScr', 1, "pre-scramble", ['', ['', 'z2', "z'", 'z', "x'", 'x'],
			['', 'z2', "z'", 'z', "x'", 'x']
		]);

		for (var i = 0; i < scrdata.length; i++) {
			select.append('<option>' + scrdata[i][0] + '</option>');
		}
		kernel.getProp('scrType', '333');

		select.change(loadSelect2);
		select2.change(function() {
			kernel.blur();
			scrLen.val(Math.abs(scrdata[select[0].selectedIndex][1][select2[0].selectedIndex][2]));
			scrLen[0].disabled = scrdata[select[0].selectedIndex][1][select2[0].selectedIndex][2] <= 0;
			genScramble();
		});
		scrLen.change(genScramble);

		var last = $('<span />').addClass('click').html(SCRAMBLE_LAST).click(function() {
			sdiv.html(lastscramble);
			if (lastscramble != undefined) {
				kernel.pushSignal('scrambleX', [lasttype, lastscramble]);
			}
		});
		var next = $('<span />').addClass('click').html(SCRAMBLE_NEXT).click(function() {
			if (sdiv.html() == lastscramble) {
				sdiv.html(scramble);
				kernel.pushSignal('scrambleX', [type, scramble]);
			} else {
				genScramble();
			}
		});
		title.append($('<nobr>').append(select, ' ', select2), " <wbr>");
		title.append($('<nobr>').append(SCRAMBLE_LENGTH + ': ', scrLen), " <wbr>");
		title.append($('<nobr>').append(last, '/', next, SCRAMBLE_SCRAMBLE));
		div.append(title, sdiv).appendTo('body');
		kernel.addWindow('scramble', BUTTON_SCRAMBLE, div, true, true, 3);
		tools.regTool('scrgen', TOOLS_SCRGEN, scrambleGenerator);
	});
	**/

	return {
		reg: regScrambler,
		scramblers: scramblers,
		mega: mega,
		formatScramble: formatScramble
	}

})(mathlib.rn, mathlib.rndEl);
