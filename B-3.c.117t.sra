
;; Function main (main, funcdef_no=1, decl_uid=2359, cgraph_uid=2, symbol_order=1) (executed once)

main ()
{
  int b;
  int a;

  <bb 2> [local count: 11059544]:

  <bb 3> [local count: 1062682282]:
  # a_12 = PHI <4(2), a_8(5)>
  # b_13 = PHI <b_3(D)(2), b_7(5)>
  b_7 = b_13 * 2;
  a_8 = a_12 + 1;
  if (a_8 != 100)
    goto <bb 5>; [98.96%]
  else
    goto <bb 4>; [1.04%]

  <bb 5> [local count: 1051622741]:
  goto <bb 3>; [100.00%]

  <bb 4> [local count: 11059544]:
  printf ("%d%d", 100, b_7);
  return 0;

}


