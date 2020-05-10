import click

@click.group()
@click.option('--removedigits/--no-removedigits', default=False, help='removes digits from string')
@click.pass_context
def hello(ctx, removedigits):
    """Supports some string commands from command line."""
    ctx.obj = removedigits


def removedigits(ctx, name):
    output=name
    if ctx.obj:
        output = [ch for ch in output if not ch.isdigit()]
    output = ''.join(output)
    return output


@hello.command('concat', help='concatnates passed in strings with delimiter')
@click.argument('argument',nargs=-1)
@click.option('-d','--delimiter',default=':',help='defaults to :')
@click.pass_context
def concat(ctx, argument,delimiter):
    argument=delimiter.join(argument)
    name = removedigits(ctx,argument)
    print(name)


@hello.command('upper', help='converts the word to upper case')
@click.argument('argument',nargs=-1)
@click.pass_context
def upper(ctx, argument):
    argument = ' '.join(argument)
    name = removedigits(ctx, argument)
    print(name.upper())


@hello.command('lower', help='converts the word to lower case')
@click.argument('argument',nargs=-1)
@click.pass_context
def lower(ctx, argument):
    argument=' '.join(argument)
    name = removedigits(ctx, argument)
    print(name.lower())


if __name__ == '__main__':
    hello()