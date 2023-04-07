
def linregress(x, y, prefix='output', xlab='x', ylab='y'):
    import matplotlib.pyplot as plt
    from scipy import stats
    import seaborn as sns

    # Set color palette to match the Lancet style
    sns.set_palette("Greys_r", 2)
    plt.rcParams.update({'font.size': 8})

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.tight_layout(pad=3)

    res = stats.linregress(x, y)
    print(f"{prefix}:R-squared: {res.rvalue ** 2:.2f}")
    print(f"{prefix}:p-value: {res.pvalue}")
    r2 = f"R2= {res.rvalue ** 2:.2f}"
    if(float(res.pvalue)) < 0.01:
        p="p<0.01"
    elif(float(res.pvalue)) < 0.05:
        p="p<0.05"
    else:
        p="ns"

    # Set the plot labels and title with appropriate font size and weight
    ax.set_xlabel(xlab, fontsize=15, fontweight='bold')
    ax.set_ylabel(ylab, fontsize=15, fontweight='bold')
    ax.set_title(prefix, fontsize=18, fontweight='bold', style='italic')

    # Plot the original data in gray
    plt.plot(x, y, 'o', label='original data', color='gray')

    # Plot the fitted line in black
    fx = [res.intercept + res.slope * i for i in x]
    plt.plot(x, fx, '-', label='fitted line ' + r2 + " " + p, color='black')

    # Add legend to the plot
    ax.legend(loc='lower right', fontsize=12)

    prefix=prefix.replace(" ","_")
    # Save figure with high resolution
    plt.savefig(prefix + '.png', dpi=300)

    # Close the figure
    plt.close()

# 自变量 物种
tax_list=[]
with open ("input/tax.input","r") as tax:
    title = tax.readline()
    x = title.strip().split("\t")[1]
    for l in tax.readlines():
        tax_list.append(float(l.strip().split("\t")[1]))
# 因变量 表型数据
env_list=[]
with open ("input/env.input","r") as env:
    title=env.readline()
    y=title.strip().split("\t")[1]
    for l in env.readlines():
        env_list.append(float(l.strip().split("\t")[1]))
linregress(tax_list,env_list,prefix='liner least squares regression',xlab=x,ylab=y)