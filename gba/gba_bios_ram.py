regs = [
    #(0x3000000, "", "User Memory and User Stack              (sp_usr=3007F00h)"),
    (0x3007f00, "", "Default Interrupt Stack (6 words/time)  (sp_irq=3007FA0h)"),
    (0x3007fa0, "", "Default Supervisor Stack (4 words/time) (sp_svc=3007FE0h)"),
    (0x3007fe0, "", "Debug Exception Stack (4 words/time)    (sp_xxx=3007FF0h)"),
    (0x3007ff0, "", "Pointer to Sound Buffer (for SWI Sound functions)"),
    #(0x3007ff4, "", "Reserved (unused)"),
    #(0x3007ff7, "", "Reserved (intro/nintendo logo related)"),
    (0x3007ff8, "", "IRQ IF Check Flags (for SWI IntrWait/VBlankIntrWait functions)"),
    (0x3007ffa, "", "Soft Reset Re-entry Flag (for SWI SoftReset function)"),
    (0x3007ffb, "", "Reserved (intro/multiboot slave related)"),
    (0x3007ffc, "", "Pointer to user IRQ handler (to 32bit ARM code)"),
]

for (ea, name, comment) in regs:
    if name:
        idc.MakeName(ea, name)
    if comment:
        idc.MakeRptCmt(ea, comment)
