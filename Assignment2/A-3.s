	.text
	.globl _main
_main:
LFB0:
	pushq	%rbp
LCFI0:
	movq	%rsp, %rbp
LCFI1:
	movl	$0, -4(%rbp)
	jmp	L2
L3:
	sall	-4(%rbp)
L2:
	cmpl	$99, -4(%rbp)
	jle	L3
	movl	$0, -8(%rbp)
	jmp	L4
L7:
	movl	$0, -12(%rbp)
	jmp	L5
L6:
	movl	-8(%rbp), %eax
	imull	-12(%rbp), %eax
	addl	%eax, -4(%rbp)
	addl	$1, -12(%rbp)
L5:
	cmpl	$49, -12(%rbp)
	jle	L6
	addl	$1, -8(%rbp)
L4:
	cmpl	$24, -8(%rbp)
	jle	L7
	movl	$0, %eax
	popq	%rbp
LCFI2:
	ret
LFE0:
	.section __TEXT,__eh_frame,coalesced,no_toc+strip_static_syms+live_support
EH_frame1:
	.set L$set$0,LECIE1-LSCIE1
	.long L$set$0
LSCIE1:
	.long	0
	.byte	0x1
	.ascii "zR\0"
	.byte	0x1
	.byte	0x78
	.byte	0x10
	.byte	0x1
	.byte	0x10
	.byte	0xc
	.byte	0x7
	.byte	0x8
	.byte	0x90
	.byte	0x1
	.align 3
LECIE1:
LSFDE1:
	.set L$set$1,LEFDE1-LASFDE1
	.long L$set$1
LASFDE1:
	.long	LASFDE1-EH_frame1
	.quad	LFB0-.
	.set L$set$2,LFE0-LFB0
	.quad L$set$2
	.byte	0
	.byte	0x4
	.set L$set$3,LCFI0-LFB0
	.long L$set$3
	.byte	0xe
	.byte	0x10
	.byte	0x86
	.byte	0x2
	.byte	0x4
	.set L$set$4,LCFI1-LCFI0
	.long L$set$4
	.byte	0xd
	.byte	0x6
	.byte	0x4
	.set L$set$5,LCFI2-LCFI1
	.long L$set$5
	.byte	0xc
	.byte	0x7
	.byte	0x8
	.align 3
LEFDE1:
	.ident	"GCC: (Homebrew GCC 10.2.0) 10.2.0"
	.subsections_via_symbols
